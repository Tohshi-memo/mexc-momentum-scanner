# Decision Report

- generated_at: 2026-06-03T03:50:34.910899+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5515**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5515, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.71% | **+0.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 977件 (Win 229 / Loss 300 / Flat 448) / skip 1099件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-03T03:50:32.576085+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.57% price=65544.6
- Funnel: target 773 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +40.29% | $13,921,572.05 |
| APR/USDT:USDT | +27.01% | $1,163,617.11 |
| GENIUS/USDT:USDT | +21.44% | $1,503,948.07 |
| BBSTOCK/USDT:USDT | +18.84% | $1,885,643.58 |
| ESPORTS/USDT:USDT | +18.08% | $4,149,351.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +3.10% | +4.67% |
| MYX/USDT:USDT | below_1h_threshold | +3.01% | +4.58% |
| EPIC/USDT:USDT | below_1h_threshold | +2.71% | +4.28% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.54% | +4.11% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.49% | +4.05% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
