# Decision Report

- generated_at: 2026-05-18T15:23:55.641588+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4447**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4447, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_BB3S | 6/18 | 33.3% | -0.04% | **-0.01%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.41% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.60% | **+1.44%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.61% | **+1.05%** |
| ASK_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.46% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.18** / 初期 $100.00 (+22.18%)
- 確定: 444件 (Win 116 / Loss 150 / Flat 178) / skip 564件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.18

## 4. Latest Market Context

- 更新: 2026-05-18T15:23:53.432624+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=76068.7
- Funnel: target 768 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +58.83% | $12,037,585.90 |
| TRAC/USDT:USDT | +31.85% | $1,234,640.49 |
| BSB/USDT:USDT | +16.36% | $12,918,424.92 |
| UP/USDT:USDT | +14.02% | $1,056,623.90 |
| OPENLEDGER/USDT:USDT | +13.41% | $1,557,878.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +1.49% | +1.88% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.26% | +1.65% |
| PLAY/USDT:USDT | below_1h_threshold | +0.72% | +1.12% |
| USOIL/USDT:USDT | below_1h_threshold | +0.61% | +1.00% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.53% | +0.92% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
