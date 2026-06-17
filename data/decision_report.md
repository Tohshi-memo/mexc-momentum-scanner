# Decision Report

- generated_at: 2026-06-17T10:05:26.608697+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6923**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6923, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +3.32% | **+1.99%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.12%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.31% | **+0.92%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| ASK_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$196.81** / 初期 $100.00 (+96.81%)
- 確定: 1796件 (Win 487 / Loss 564 / Flat 745) / skip 1688件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $196.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.31** / 初期 $100.00 (+1.31%)
- 確定: 196件 (Win 45 / Loss 41 / Flat 110) / skip 138件
- 成長率目線: 平均log +0.000067 / 幾何平均 +0.007% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1257 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $101.31

## 5. Latest Market Context

- 更新: 2026-06-17T10:05:22.399565+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=64824.9
- Funnel: target 784 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +44.29% | $6,014,974.10 |
| HIGH/USDT:USDT | +40.06% | $2,584,503.74 |
| SQD/USDT:USDT | +21.65% | $2,709,384.80 |
| ID/USDT:USDT | +21.41% | $1,230,516.72 |
| UNI/USDT:USDT | +20.35% | $56,558,708.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +1.24% | +1.32% |
| STG/USDT:USDT | below_1h_threshold | +0.81% | +0.89% |
| ROAM/USDT:USDT | below_1h_threshold | +0.71% | +0.79% |
| PLAY/USDT:USDT | below_1h_threshold | +0.70% | +0.79% |
| BTW/USDT:USDT | below_1h_threshold | +0.69% | +0.77% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
