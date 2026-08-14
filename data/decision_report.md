# Decision Report

- generated_at: 2026-08-14T10:31:34.513787+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11533**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11533, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.88% | **+0.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.59% | **+1.12%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.62% | **+0.81%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$622.46** / 初期 $100.00 (+522.46%)
- 確定: 4001件 (Win 1251 / Loss 1312 / Flat 1438) / skip 4093件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $622.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3293件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0629 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.59** / 初期 $100.00 (+17.59%)
- 確定: 1494件 (Win 447 / Loss 566 / Flat 481) / pending 3件 / skip 1507件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.59

## 6. Latest Market Context

- 更新: 2026-08-14T10:31:23.953659+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=62871.3
- Funnel: target 981 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.6 >= 65=1, 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +70.10% | $15,353,136.59 |
| AKE/USDT:USDT | +48.82% | $70,691,483.37 |
| VELVET/USDT:USDT | +37.66% | $30,694,686.95 |
| 2Z/USDT:USDT | +21.16% | $1,631,043.26 |
| WDAYSTOCK/USDT:USDT | +19.83% | $1,650,701.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVAAI/USDT:USDT | below_1h_threshold | +4.16% | +3.99% |
| VELVET/USDT:USDT | below_1h_threshold | +3.54% | +3.37% |
| SNXX/USDT:USDT | below_1h_threshold | +3.36% | +3.18% |
| 2Z/USDT:USDT | below_1h_threshold | +3.06% | +2.89% |
| APR/USDT:USDT | below_1h_threshold | +2.53% | +2.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
