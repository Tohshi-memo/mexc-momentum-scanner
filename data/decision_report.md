# Decision Report

- generated_at: 2026-07-31T16:36:18.088981+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10017**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10017, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.49% | **+0.34%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.94% | **+1.18%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.64% | **+0.82%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$547.70** / 初期 $100.00 (+447.70%)
- 確定: 3573件 (Win 1141 / Loss 1168 / Flat 1264) / skip 3005件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $547.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2150件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.49** / 初期 $100.00 (+11.49%)
- 確定: 847件 (Win 274 / Loss 335 / Flat 238) / pending 6件 / skip 639件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000173 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $111.49

## 6. Latest Market Context

- 更新: 2026-07-31T16:36:10.789222+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=62812.9
- Funnel: target 921 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +5.47% | $15,346,159.01 |
| KOMA/USDT:USDT | +4.49% | $15,360,077.05 |
| PUMPFUN/USDT:USDT | +4.39% | $42,220,361.34 |
| SNXX/USDT:USDT | +4.23% | $18,003,541.25 |
| BANK/USDT:USDT | +4.03% | $48,339,321.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KOMA/USDT:USDT | below_1h_threshold | +4.49% | +4.30% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +4.20% | +4.02% |
| BANK/USDT:USDT | below_1h_threshold | +4.04% | +3.85% |
| KAITO/USDT:USDT | below_1h_threshold | +3.69% | +3.51% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.95% | +2.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
