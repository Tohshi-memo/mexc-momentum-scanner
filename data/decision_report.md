# Decision Report

- generated_at: 2026-07-19T15:31:10.920984+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9052**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=9052, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.65% | **+1.32%** |
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.62% | **+0.65%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.88% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.59% | **+1.25%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.16% | **+0.06%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$397.32** / 初期 $100.00 (+297.32%)
- 確定: 3114件 (Win 977 / Loss 995 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $397.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.70** / 初期 $100.00 (+26.70%)
- 確定: 1013件 (Win 262 / Loss 215 / Flat 536) / skip 1450件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0566 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $126.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.66** / 初期 $100.00 (+0.66%)
- 確定: 252件 (Win 86 / Loss 126 / Flat 40) / pending 3件 / skip 267件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000338 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.66

## 6. Latest Market Context

- 更新: 2026-07-19T15:31:04.357924+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=64467.3
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +106.06% | $52,144,458.41 |
| TLM/USDT:USDT | +80.89% | $9,757,164.26 |
| B/USDT:USDT | +50.03% | $33,715,659.57 |
| TAG/USDT:USDT | +25.60% | $4,987,267.36 |
| KAITO/USDT:USDT | +15.48% | $3,260,173.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.66% | +2.80% |
| KAITO/USDT:USDT | below_1h_threshold | +2.53% | +2.67% |
| TAG/USDT:USDT | below_1h_threshold | +1.86% | +2.01% |
| JTO/USDT:USDT | below_1h_threshold | +1.73% | +1.88% |
| ARB/USDT:USDT | below_1h_threshold | +1.32% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
