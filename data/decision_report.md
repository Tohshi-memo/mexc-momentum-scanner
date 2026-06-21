# Decision Report

- generated_at: 2026-06-21T02:06:19.368644+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7287**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7287, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.05% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.81% | **+1.97%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.85% | **+1.57%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.64% | **+1.23%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.43% | **+1.09%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.95% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$102.46** / 初期 $100.00 (+2.46%)
- 確定トレード: 25件 (TP 10 / SL 15 / EXP 0)
- 最新: AGT/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$236.20** / 初期 $100.00 (+136.20%)
- 確定: 2016件 (Win 597 / Loss 661 / Flat 758) / skip 1832件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAND/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $236.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 388件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0288 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T02:06:15.128770+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64213.9
- Funnel: target 796 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +48.90% | $48,053,472.41 |
| ALICE/USDT:USDT | +42.11% | $2,916,384.63 |
| RESOLV/USDT:USDT | +26.99% | $3,509,177.54 |
| VELVET/USDT:USDT | +12.31% | $16,920,340.73 |
| ASTEROID/USDT:USDT | +9.86% | $1,557,807.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALICE/USDT:USDT | below_1h_threshold | +2.92% | +2.93% |
| BICO/USDT:USDT | below_1h_threshold | +2.10% | +2.11% |
| JTO/USDT:USDT | below_1h_threshold | +1.24% | +1.25% |
| SLX/USDT:USDT | below_1h_threshold | +1.08% | +1.09% |
| RESOLV/USDT:USDT | below_1h_threshold | +1.00% | +1.02% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
