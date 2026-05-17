# Decision Report

- generated_at: 2026-05-17T22:38:28.375327+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4423**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4423, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 4/14 | 28.6% | +1.43% | **+0.41%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.17% | **-0.06%** |
| ASK | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.07% | **+1.45%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.77% | **+1.24%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.70% | **+1.19%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.94% | **+0.52%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.97** / 初期 $100.00 (+21.97%)
- 確定: 420件 (Win 110 / Loss 142 / Flat 168) / skip 564件
- 成長率目線: 平均log +0.000473 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $121.97

## 4. Latest Market Context

- 更新: 2026-05-17T22:38:26.160723+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.53% price=77952.5
- Funnel: target 760 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +28.47% | $3,096,583.64 |
| UB/USDT:USDT | +12.49% | $14,206,401.02 |
| BUILDONBOB/USDT:USDT | +12.17% | $1,276,413.83 |
| BILL/USDT:USDT | +7.75% | $34,492,425.81 |
| HYPE/USDT:USDT | +7.07% | $295,242,589.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SILVER/USDT:USDT | below_1h_threshold | +1.35% | +1.88% |
| SPACE/USDT:USDT | below_1h_threshold | +1.17% | +1.70% |
| NMR/USDT:USDT | below_1h_threshold | +1.10% | +1.62% |
| XPD/USDT:USDT | below_1h_threshold | +1.03% | +1.56% |
| USOIL/USDT:USDT | below_1h_threshold | +0.82% | +1.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
