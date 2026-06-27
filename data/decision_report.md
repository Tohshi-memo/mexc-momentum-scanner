# Decision Report

- generated_at: 2026-06-27T08:05:07.394075+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7679**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7679, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.46% | **+0.07%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.80% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.08% | **+1.35%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.55% | **+1.24%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.19% | **+1.10%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.55% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.23** / 初期 $100.00 (+137.23%)
- 確定: 2204件 (Win 662 / Loss 735 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $237.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.76** / 初期 $100.00 (+8.76%)
- 確定: 410件 (Win 113 / Loss 102 / Flat 195) / skip 680件
- 成長率目線: 平均log +0.000205 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0713 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $108.76

## 5. Latest Market Context

- 更新: 2026-06-27T08:05:01.737976+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=60443.4
- Funnel: target 806 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MYX/USDT:USDT | +35.52% | $9,731,208.76 |
| VELVET/USDT:USDT | +34.48% | $61,150,885.18 |
| PUNDIX/USDT:USDT | +18.29% | $6,159,434.49 |
| SYRUP/USDT:USDT | +18.07% | $1,648,669.31 |
| SLX/USDT:USDT | +14.69% | $10,528,523.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +2.93% | +3.06% |
| VELVET/USDT:USDT | below_1h_threshold | +2.59% | +2.72% |
| SYN/USDT:USDT | below_1h_threshold | +1.48% | +1.61% |
| SNT/USDT:USDT | below_1h_threshold | +0.43% | +0.56% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.42% | +0.55% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
