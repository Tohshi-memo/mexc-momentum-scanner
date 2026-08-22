# Decision Report

- generated_at: 2026-08-22T01:36:22.701922+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12285**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12285, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.76% | **-1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +3.70% | **+1.48%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.43% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +4.44% | **+3.11%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.70% | **+2.96%** |
| MARKET_LONG | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.46% | **+1.73%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +4.06% | **+1.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$688.13** / 初期 $100.00 (+588.13%)
- 確定: 4404件 (Win 1348 / Loss 1440 / Flat 1616) / skip 4442件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $688.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.78** / 初期 $100.00 (+54.78%)
- 確定: 1891件 (Win 521 / Loss 452 / Flat 918) / skip 3805件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1787 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.35% 残高後 $154.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.57** / 初期 $100.00 (+17.57%)
- 確定: 1835件 (Win 544 / Loss 695 / Flat 596) / pending 5件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000418 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT` SL_HIT account -0.17% 残高後 $117.57

## 6. Latest Market Context

- 更新: 2026-08-22T01:36:12.012766+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=78072.3
- Funnel: target 1018 → liquid 217 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +281.44% | $3,659,830.24 |
| CATE/USDT:USDT | +69.46% | $12,104,087.50 |
| AGI/USDT:USDT | +29.98% | $1,724,513.10 |
| JIMOTHY/USDT:USDT | +19.95% | $1,658,266.99 |
| ETC/USDT:USDT | +19.28% | $9,888,797.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +3.15% | +2.95% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.76% | +2.56% |
| PYTH/USDT:USDT | below_1h_threshold | +2.75% | +2.55% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.42% | +2.23% |
| CATE/USDT:USDT | below_1h_threshold | +2.23% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
