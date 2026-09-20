# Decision Report

- generated_at: 2026-09-20T10:41:48.632730+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15171**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15171, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.76% | **-1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_8PCT | 7/20 | 35.0% | +0.53% | **+0.19%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.17% | **+0.08%** |
| LIMIT_7PCT | 8/20 | 40.0% | -0.15% | **-0.06%** |
| LIMIT_9PCT | 6/20 | 30.0% | -0.57% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.26% | **+1.69%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.56% | **+1.67%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.88% | **+1.59%** |
| LIMIT_BB3S_LONG | 3/10 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.31% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,210.73** / 初期 $100.00 (+1110.73%)
- 確定: 5697件 (Win 1704 / Loss 1837 / Flat 2156) / skip 6035件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,210.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3279件 (Win 910 / Loss 764 / Flat 1605) / skip 5303件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0262 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3671件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000124 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T10:41:32.554856+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=80294.4
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1, 4h RSI 75.4 >= 65=1, 4h RSI 75.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +63.46% | $6,969,807.08 |
| AKE/USDT:USDT | +41.83% | $74,917,594.70 |
| ONE/USDT:USDT | +31.54% | $53,303,008.57 |
| BTW/USDT:USDT | +24.22% | $2,013,821.01 |
| OFC/USDT:USDT | +23.11% | $2,465,491.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +3.01% | +3.19% |
| AKE/USDT:USDT | below_1h_threshold | +2.28% | +2.45% |
| VVV/USDT:USDT | below_1h_threshold | +1.97% | +2.15% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.32% | +1.50% |
| ENA/USDT:USDT | below_1h_threshold | +0.20% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
