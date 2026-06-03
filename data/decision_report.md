# Decision Report

- generated_at: 2026-06-03T08:43:34.771041+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5537**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5537, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.20% | **-1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 17/20 | 85.0% | +1.41% | **+1.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.48% | **+0.41%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.72% | **+0.86%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.44% | **+0.42%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.37% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.88** / 初期 $100.00 (+30.88%)
- 確定: 991件 (Win 235 / Loss 306 / Flat 450) / skip 1107件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $130.88

## 4. Latest Market Context

- 更新: 2026-06-03T08:43:29.456661+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=66991.4
- Funnel: target 771 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +40.01% | $3,580,479.85 |
| PORTAL/USDT:USDT | +33.86% | $14,629,555.88 |
| GENIUS/USDT:USDT | +28.77% | $1,907,902.81 |
| LIT/USDT:USDT | +24.75% | $8,395,530.30 |
| ENA/USDT:USDT | +24.72% | $49,502,815.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +3.85% | +4.14% |
| US/USDT:USDT | below_1h_threshold | +3.84% | +4.13% |
| GUA/USDT:USDT | below_1h_threshold | +2.87% | +3.17% |
| MYX/USDT:USDT | below_1h_threshold | +2.80% | +3.09% |
| ZORA/USDT:USDT | below_1h_threshold | +2.01% | +2.30% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
