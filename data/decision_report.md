# Decision Report

- generated_at: 2026-11-04T23:46:19.074271+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18143**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18143, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.69% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.28% | **+1.37%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.09% | **+1.15%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.37% | **+1.07%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.08% | **+0.86%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.56% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,512.04** / 初期 $100.00 (+1412.04%)
- 確定: 6962件 (Win 2014 / Loss 2235 / Flat 2713) / skip 7742件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FARTCOIN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,512.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$374.93** / 初期 $100.00 (+274.93%)
- 確定: 4552件 (Win 1222 / Loss 1027 / Flat 2303) / skip 7002件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FARTCOIN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $374.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6305件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000153 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T23:46:06.581695+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80646.8
- Funnel: target 1078 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELSA/USDT:USDT | +31.08% | $1,769,683.02 |
| APPSTOCK/USDT:USDT | +22.37% | $1,163,789.35 |
| FLUID/USDT:USDT | +12.44% | $3,345,897.04 |
| AXTISTOCK/USDT:USDT | +5.64% | $2,248,154.48 |
| BAT/USDT:USDT | +4.96% | $1,789,077.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APPSTOCK/USDT:USDT | below_1h_threshold | +3.19% | +3.24% |
| ICNT/USDT:USDT | below_1h_threshold | +1.25% | +1.30% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.94% | +0.98% |
| JCT/USDT:USDT | below_1h_threshold | +0.65% | +0.69% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.60% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
