# Decision Report

- generated_at: 2026-08-20T20:31:33.748396+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12086**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12086, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.10% | **+0.51%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_BB3S | 8/15 | 53.3% | +0.73% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.22% | **+2.89%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.38% | **+2.36%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.01% | **+2.25%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.39% | **+1.56%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$633.07** / 初期 $100.00 (+533.07%)
- 確定: 4299件 (Win 1317 / Loss 1404 / Flat 1578) / skip 4348件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $633.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3675件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1471 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.58** / 初期 $100.00 (+17.58%)
- 確定: 1778件 (Win 530 / Loss 676 / Flat 572) / pending 6件 / skip 1778件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.58

## 6. Latest Market Context

- 更新: 2026-08-20T20:31:20.085592+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=72779.5
- Funnel: target 1011 → liquid 199 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.3 >= 65=1, 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +50.62% | $2,588,678.72 |
| ONG/USDT:USDT | +43.02% | $7,245,677.39 |
| PEOPLE/USDT:USDT | +13.16% | $2,718,522.43 |
| TUT/USDT:USDT | +11.66% | $5,218,028.99 |
| BLESS/USDT:USDT | +7.41% | $2,828,254.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.66% | +4.49% |
| CRV/USDT:USDT | below_1h_threshold | +4.47% | +4.30% |
| MVLL/USDT:USDT | below_1h_threshold | +3.56% | +3.39% |
| MUU/USDT:USDT | below_1h_threshold | +3.38% | +3.20% |
| RCATSTOCK/USDT:USDT | below_1h_threshold | +2.82% | +2.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
