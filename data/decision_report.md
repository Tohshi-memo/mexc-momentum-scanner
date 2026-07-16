# Decision Report

- generated_at: 2026-07-16T13:31:07.235405+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8808**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8808, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.31% | **+0.21%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.80% | **+0.53%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.76% | **+0.45%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.05% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$109.02** / 初期 $100.00 (+9.02%)
- 確定トレード: 106件 (TP 40 / SL 64 / EXP 2)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$338.75** / 初期 $100.00 (+238.75%)
- 確定: 2923件 (Win 911 / Loss 945 / Flat 1067) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $338.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.12** / 初期 $100.00 (+7.12%)
- 確定: 770件 (Win 178 / Loss 170 / Flat 422) / skip 1449件
- 成長率目線: 平均log +0.000089 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0026 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$97.78** / 初期 $100.00 (-2.22%)
- 確定: 77件 (Win 22 / Loss 51 / Flat 4) / pending 2件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000324 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $97.78

## 6. Latest Market Context

- 更新: 2026-07-16T13:31:00.761769+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.58% price=64307.1
- Funnel: target 880 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +36.34% | $4,218,064.01 |
| AKE/USDT:USDT | +25.47% | $45,743,188.92 |
| ROAM/USDT:USDT | +21.03% | $6,021,473.02 |
| US/USDT:USDT | +20.45% | $16,696,789.59 |
| BANK/USDT:USDT | +20.35% | $4,448,495.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.36% | +3.78% |
| ROAM/USDT:USDT | below_1h_threshold | +3.42% | +2.84% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.30% | +1.72% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.06% | +1.48% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.81% | +1.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
