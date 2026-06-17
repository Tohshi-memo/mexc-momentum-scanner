# Decision Report

- generated_at: 2026-06-17T05:31:52.541229+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6906**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6906, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.22% | **-2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.10% | **-0.05%** |
| LIMIT_BB3S | 4/16 | 25.0% | -1.50% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.63% | **+2.82%** |
| MARKET_LONG | 20/20 | 100.0% | +2.40% | **+2.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.72% | **+1.77%** |
| LIMIT_2PCT_LONG | 7/20 | 35.0% | +0.61% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$195.87** / 初期 $100.00 (+95.87%)
- 確定: 1779件 (Win 479 / Loss 556 / Flat 744) / skip 1688件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SQD/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $195.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.99** / 初期 $100.00 (-0.01%)
- 確定: 179件 (Win 38 / Loss 34 / Flat 107) / skip 138件
- 成長率目線: 平均log -0.000000 / 幾何平均 -0.000% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0919 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SQD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $99.99

## 5. Latest Market Context

- 更新: 2026-06-17T05:31:47.058238+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=65819.1
- Funnel: target 785 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +32.15% | $10,910,772.62 |
| SQD/USDT:USDT | +26.78% | $1,566,576.13 |
| SPX/USDT:USDT | +25.36% | $7,500,996.86 |
| ESPORTS/USDT:USDT | +23.69% | $3,984,521.42 |
| UNI/USDT:USDT | +15.95% | $45,714,076.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +3.50% | +3.55% |
| COAI/USDT:USDT | below_1h_threshold | +2.14% | +2.19% |
| H/USDT:USDT | below_1h_threshold | +1.51% | +1.56% |
| SPX/USDT:USDT | below_1h_threshold | +1.40% | +1.45% |
| RAVE/USDT:USDT | below_1h_threshold | +1.35% | +1.40% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
