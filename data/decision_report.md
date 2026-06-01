# Decision Report

- generated_at: 2026-06-01T00:56:42.561570+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5248**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5248, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.39% | **+0.88%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.32% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/11 | 63.6% | +3.62% | **+2.30%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.93% | **+1.64%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.24% | **+1.62%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.48% | **+1.49%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.50% | **+1.43%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.91** / 初期 $100.00 (+34.91%)
- 確定: 883件 (Win 206 / Loss 261 / Flat 416) / skip 926件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $134.91

## 4. Latest Market Context

- 更新: 2026-06-01T00:56:38.880456+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=73884.9
- Funnel: target 775 → liquid 134 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.1 >= 65=1, 4h RSI 81.5 >= 65=1, 4h RSI 76.8 >= 65=1, 4h RSI 74.8 >= 65=1, 4h RSI 88.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +177.94% | $23,120,872.06 |
| H/USDT:USDT | +33.29% | $14,061,292.58 |
| STG/USDT:USDT | +28.44% | $21,807,120.92 |
| LAB/USDT:USDT | +23.71% | $193,860,503.01 |
| ZORA/USDT:USDT | +20.62% | $1,782,081.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.26% | +3.95% |
| AIA/USDT:USDT | below_1h_threshold | +3.84% | +3.53% |
| ORDI/USDT:USDT | below_1h_threshold | +2.87% | +2.56% |
| VVV/USDT:USDT | below_1h_threshold | +2.81% | +2.49% |
| CTR/USDT:USDT | below_1h_threshold | +2.81% | +2.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
