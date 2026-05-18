# Decision Report

- generated_at: 2026-05-18T05:38:37.941517+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4436**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4436, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.16% | **+0.06%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.64% | **+0.38%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.63% | **+0.38%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.38% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$96.22** / 初期 $100.00 (-3.78%)
- 確定トレード: 52件 (TP 13 / SL 36 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.78** / 初期 $100.00 (+20.78%)
- 確定: 433件 (Win 112 / Loss 147 / Flat 174) / skip 564件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $120.78

## 4. Latest Market Context

- 更新: 2026-05-18T05:38:35.470281+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=76951.0
- Funnel: target 765 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +38.31% | $6,341,182.21 |
| BSB/USDT:USDT | +7.97% | $19,586,894.94 |
| AKT/USDT:USDT | +5.94% | $1,514,519.03 |
| HYPE/USDT:USDT | +5.17% | $280,439,631.13 |
| ZEC/USDT:USDT | +4.39% | $488,466,264.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.35% | +4.41% |
| LAB/USDT:USDT | below_1h_threshold | +3.29% | +3.35% |
| RIVER/USDT:USDT | below_1h_threshold | +0.76% | +0.82% |
| XPD/USDT:USDT | below_1h_threshold | +0.19% | +0.26% |
| COPPER/USDT:USDT | below_1h_threshold | +0.19% | +0.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
