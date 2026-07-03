# Decision Report

- generated_at: 2026-07-03T11:01:16.356228+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8153**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=8153, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_BB3S | 2/17 | 11.8% | -1.09% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.40% | **+0.70%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.77% | **+0.39%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.30% | **+0.15%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.02% | **-0.01%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$283.00** / 初期 $100.00 (+183.00%)
- 確定: 2474件 (Win 760 / Loss 826 / Flat 888) / skip 2240件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $283.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.66** / 初期 $100.00 (+5.66%)
- 確定: 600件 (Win 144 / Loss 143 / Flat 313) / skip 964件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.35% 残高後 $105.66

## 5. Latest Market Context

- 更新: 2026-07-03T11:01:11.458718+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=61850.1
- Funnel: target 834 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +56.84% | $2,406,928.87 |
| ARPA/USDT:USDT | +40.09% | $2,811,052.20 |
| RIF/USDT:USDT | +32.62% | $8,160,309.80 |
| ZKP/USDT:USDT | +31.74% | $4,472,971.95 |
| THE/USDT:USDT | +25.39% | $2,827,690.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +2.51% | +2.57% |
| NEX/USDT:USDT | below_1h_threshold | +0.90% | +0.96% |
| GUA/USDT:USDT | below_1h_threshold | +0.83% | +0.89% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.71% | +0.77% |
| ALLO/USDT:USDT | below_1h_threshold | +0.46% | +0.51% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
