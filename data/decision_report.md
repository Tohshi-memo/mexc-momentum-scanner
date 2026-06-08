# Decision Report

- generated_at: 2026-06-08T02:19:36.848789+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6022**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6022, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.01% | **+0.50%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 2/18 | 11.1% | +1.81% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.97% | **+0.44%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.44% | **+0.42%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$99.07** / 初期 $100.00 (-0.93%)
- 確定トレード: 6件 (TP 1 / SL 4 / EXP 1)
- 最新: LUNC/USDT:USDT EXPIRED PnL +0.53% 残高後 $99.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$152.15** / 初期 $100.00 (+52.15%)
- 確定: 1139件 (Win 278 / Loss 347 / Flat 514) / skip 1444件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $152.15

## 4. Latest Market Context

- 更新: 2026-06-08T02:19:33.580732+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=62959.1
- Funnel: target 773 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +28.79% | $1,637,266.49 |
| BEAT/USDT:USDT | +27.44% | $91,993,034.94 |
| BANK/USDT:USDT | +23.50% | $4,681,000.36 |
| BLESS/USDT:USDT | +23.24% | $8,261,369.84 |
| PIPPIN/USDT:USDT | +22.94% | $6,421,516.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +2.47% | +2.83% |
| EPIC/USDT:USDT | below_1h_threshold | +2.38% | +2.74% |
| NEAR/USDT:USDT | below_1h_threshold | +1.67% | +2.03% |
| BABY/USDT:USDT | below_1h_threshold | +1.10% | +1.47% |
| INJ/USDT:USDT | below_1h_threshold | +1.00% | +1.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
