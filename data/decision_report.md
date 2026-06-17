# Decision Report

- generated_at: 2026-06-17T08:30:42.892905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6916**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6916, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.03% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +5.96% | **+2.38%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| ASK_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.38% | **+0.97%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.81** / 初期 $100.00 (+98.81%)
- 確定: 1789件 (Win 485 / Loss 559 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $198.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 189件 (Win 42 / Loss 37 / Flat 110) / skip 138件
- 成長率目線: 平均log +0.000048 / 幾何平均 +0.005% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0987 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $100.91

## 5. Latest Market Context

- 更新: 2026-06-17T08:30:35.464222+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=65270.7
- Funnel: target 784 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +43.96% | $5,029,884.96 |
| ROAM/USDT:USDT | +33.22% | $3,072,777.86 |
| SQD/USDT:USDT | +21.31% | $2,460,266.91 |
| UNI/USDT:USDT | +17.51% | $53,228,277.26 |
| SPX/USDT:USDT | +15.66% | $8,920,832.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROAM/USDT:USDT | below_1h_threshold | +4.83% | +5.19% |
| PLAY/USDT:USDT | below_1h_threshold | +2.30% | +2.66% |
| LIT/USDT:USDT | below_1h_threshold | +1.09% | +1.45% |
| GUA/USDT:USDT | below_1h_threshold | +0.91% | +1.27% |
| HIGH/USDT:USDT | below_1h_threshold | +0.68% | +1.03% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
