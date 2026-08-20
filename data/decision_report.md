# Decision Report

- generated_at: 2026-08-20T20:26:37.782186+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12085**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12085, expectancy=-0.00%
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
| LIMIT_BB3S | 7/14 | 50.0% | +1.24% | **+0.62%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.10% | **+0.51%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.11% | **+2.64%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.08% | **+2.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.78% | **+1.95%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.29% | **+1.65%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$629.10** / 初期 $100.00 (+529.10%)
- 確定: 4298件 (Win 1316 / Loss 1404 / Flat 1578) / skip 4348件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $629.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3674件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1291 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.27** / 初期 $100.00 (+17.27%)
- 確定: 1777件 (Win 529 / Loss 676 / Flat 572) / pending 6件 / skip 1777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000278 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.27

## 6. Latest Market Context

- 更新: 2026-08-20T20:26:25.298265+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=72793.0
- Funnel: target 1011 → liquid 198 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.4 >= 65=1, 4h RSI 81.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +55.96% | $2,535,884.34 |
| ONG/USDT:USDT | +43.87% | $6,838,732.43 |
| PEOPLE/USDT:USDT | +13.30% | $2,697,484.24 |
| TUT/USDT:USDT | +11.34% | $5,181,170.70 |
| ENA/USDT:USDT | +7.31% | $30,951,457.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRV/USDT:USDT | below_1h_threshold | +4.14% | +3.94% |
| MVLL/USDT:USDT | below_1h_threshold | +3.56% | +3.37% |
| MUU/USDT:USDT | below_1h_threshold | +3.38% | +3.18% |
| RCATSTOCK/USDT:USDT | below_1h_threshold | +2.82% | +2.63% |
| CYS/USDT:USDT | below_1h_threshold | +2.24% | +2.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
