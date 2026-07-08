# Decision Report

- generated_at: 2026-07-08T22:01:40.047983+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8508**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8508, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.51% | **+0.31%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.26% | **+0.43%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.71% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$104.10** / 初期 $100.00 (+4.10%)
- 確定トレード: 80件 (TP 29 / SL 50 / EXP 1)
- 最新: ALLO/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.08** / 初期 $100.00 (+220.08%)
- 確定: 2696件 (Win 852 / Loss 903 / Flat 941) / skip 2373件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $320.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1277件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0592 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-08T22:01:34.976058+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=62194.3
- Funnel: target 851 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +62.00% | $3,032,604.91 |
| LAB/USDT:USDT | +28.18% | $56,224,464.74 |
| OGN/USDT:USDT | +20.13% | $3,854,013.09 |
| ALLO/USDT:USDT | +12.91% | $11,339,241.81 |
| KORU/USDT:USDT | +11.58% | $7,188,502.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.25% | +3.19% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.36% | +1.31% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.24% | +1.19% |
| BEAT/USDT:USDT | below_1h_threshold | +0.95% | +0.90% |
| TAG/USDT:USDT | below_1h_threshold | +0.89% | +0.83% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
