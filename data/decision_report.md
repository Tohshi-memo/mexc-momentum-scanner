# Decision Report

- generated_at: 2026-09-09T14:56:48.363002+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14078**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14078, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.19% | **-1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.71% | **+0.94%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.28% | **+0.58%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.39% | **+1.91%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.64% | **+1.72%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5326件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$192.04** / 初期 $100.00 (+92.04%)
- 確定: 2672件 (Win 735 / Loss 627 / Flat 1310) / skip 4817件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0530 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $192.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.84** / 初期 $100.00 (+17.84%)
- 確定: 2620件 (Win 765 / Loss 1001 / Flat 854) / pending 0件 / skip 2935件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZEC/USDT:USDT `MARKET` EXPIRED account -0.09% 残高後 $117.84

## 6. Latest Market Context

- 更新: 2026-09-09T14:56:30.832915+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=78895.4
- Funnel: target 1064 → liquid 162 → pre 50 → checked 50 → surge 7 → strict 1
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.7 >= 65=1, 4h RSI 71.9 >= 65=1, 4h RSI 72.7 >= 65=1, 4h RSI 80.2 >= 65=1, 4h RSI 74.0 >= 65=1, 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +62.47% | $1,881,910.37 |
| IOST/USDT:USDT | +54.74% | $10,084,304.03 |
| RAY/USDT:USDT | +25.91% | $7,018,375.39 |
| OL/USDT:USDT | +18.69% | $2,539,282.19 |
| BR/USDT:USDT | +18.25% | $2,168,353.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.84% | +5.12% |
| KORU/USDT:USDT | below_1h_threshold | +4.26% | +4.53% |
| MAGMA/USDT:USDT | below_1h_threshold | +4.15% | +4.42% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +3.82% | +4.10% |
| ZEN/USDT:USDT | below_1h_threshold | +3.06% | +3.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
