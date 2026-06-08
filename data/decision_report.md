# Decision Report

- generated_at: 2026-06-08T01:44:17.179601+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6018**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6018, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.17% | **-2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.32% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 2/16 | 12.5% | +1.81% | **+0.23%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.03% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.90% | **+1.81%** |
| ASK_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| MARKET_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.23% | **+1.13%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.50% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$99.07** / 初期 $100.00 (-0.93%)
- 確定トレード: 6件 (TP 1 / SL 4 / EXP 1)
- 最新: LUNC/USDT:USDT EXPIRED PnL +0.53% 残高後 $99.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$155.23** / 初期 $100.00 (+55.23%)
- 確定: 1135件 (Win 278 / Loss 343 / Flat 514) / skip 1444件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $155.23

## 4. Latest Market Context

- 更新: 2026-06-08T01:44:10.233503+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.84% price=63061.7
- Funnel: target 773 → liquid 142 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1, 4h RSI 70.3 >= 65=1, 4h RSI 82.3 >= 65=1, 4h RSI 75.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +39.06% | $8,024,018.95 |
| BEAT/USDT:USDT | +35.59% | $89,402,627.03 |
| BANK/USDT:USDT | +34.49% | $4,631,559.12 |
| EPIC/USDT:USDT | +25.85% | $1,546,507.68 |
| PIPPIN/USDT:USDT | +23.08% | $6,357,593.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.75% | +5.60% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.76% | +3.61% |
| OPENAI/USDT:USDT | below_1h_threshold | +1.88% | +2.73% |
| MYX/USDT:USDT | below_1h_threshold | +1.60% | +2.44% |
| CTR/USDT:USDT | below_1h_threshold | +1.47% | +2.32% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
