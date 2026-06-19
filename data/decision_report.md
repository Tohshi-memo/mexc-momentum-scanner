# Decision Report

- generated_at: 2026-06-19T19:05:34.270464+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7166**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7166, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.21% | **-1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.33% | **+0.13%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.12% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.33% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.47% | **+1.24%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.50% | **+1.12%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.16% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$227.11** / 初期 $100.00 (+127.11%)
- 確定: 1968件 (Win 571 / Loss 639 / Flat 758) / skip 1759件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $227.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 267件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0795 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T19:05:29.004205+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63087.9
- Funnel: target 795 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +25.99% | $7,782,083.25 |
| BLESS/USDT:USDT | +23.44% | $3,089,770.08 |
| BSB/USDT:USDT | +15.96% | $19,373,726.32 |
| MYX/USDT:USDT | +9.44% | $3,266,538.40 |
| BTW/USDT:USDT | +8.32% | $5,646,103.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +1.41% | +1.40% |
| TWLOSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.17% |
| RIF/USDT:USDT | below_1h_threshold | +0.93% | +0.92% |
| BICO/USDT:USDT | below_1h_threshold | +0.91% | +0.90% |
| VVV/USDT:USDT | below_1h_threshold | +0.87% | +0.86% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
