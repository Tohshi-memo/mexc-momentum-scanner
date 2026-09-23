# Decision Report

- generated_at: 2026-09-23T07:26:32.875598+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15410**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15410, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.37% | **-1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.40% | **+2.04%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.44% | **+1.63%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.90% | **+1.43%** |
| MARKET_LONG | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.82% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,187.35** / 初期 $100.00 (+1087.35%)
- 確定: 5883件 (Win 1735 / Loss 1884 / Flat 2264) / skip 6088件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAKE/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $1,187.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.32** / 初期 $100.00 (+148.32%)
- 確定: 3362件 (Win 928 / Loss 784 / Flat 1650) / skip 5459件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $248.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.98** / 初期 $100.00 (+20.98%)
- 確定: 3133件 (Win 921 / Loss 1233 / Flat 979) / pending 3件 / skip 3752件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000107 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $120.98

## 6. Latest Market Context

- 更新: 2026-09-23T07:26:18.917443+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=86294.6
- Funnel: target 1061 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +158.34% | $1,198,441.88 |
| SHROOM/USDT:USDT | +73.58% | $1,293,215.04 |
| LONGXIA/USDT:USDT | +25.74% | $1,758,198.46 |
| NIL/USDT:USDT | +25.25% | $8,140,207.69 |
| SAGA/USDT:USDT | +23.28% | $1,762,466.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000BONK/USDT:USDT | below_1h_threshold | +2.55% | +2.70% |
| MYX/USDT:USDT | below_1h_threshold | +1.87% | +2.02% |
| HNT/USDT:USDT | below_1h_threshold | +1.70% | +1.85% |
| ALLO/USDT:USDT | below_1h_threshold | +1.19% | +1.35% |
| TUT/USDT:USDT | below_1h_threshold | +0.78% | +0.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
