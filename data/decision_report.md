# Decision Report

- generated_at: 2026-09-20T10:56:48.374468+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15173**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15173, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 6/20 | 30.0% | +0.83% | **+0.25%** |
| LIMIT_8PCT | 7/20 | 35.0% | +0.53% | **+0.19%** |
| LIMIT_6PCT | 10/20 | 50.0% | +0.17% | **+0.08%** |
| LIMIT_7PCT | 8/20 | 40.0% | -0.15% | **-0.06%** |
| LIMIT_9PCT | 6/20 | 30.0% | -0.57% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.82% | **+2.12%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.63% | **+2.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,204.68** / 初期 $100.00 (+1104.68%)
- 確定: 5699件 (Win 1704 / Loss 1838 / Flat 2157) / skip 6035件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,204.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3280件 (Win 910 / Loss 764 / Flat 1606) / skip 5304件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0262 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAG/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3672件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000107 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T10:56:33.458632+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=80318.7
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.6 >= 65=1, 4h RSI 76.0 >= 65=1, 4h RSI 76.4 >= 65=1, 4h RSI 66.3 >= 65=1, 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +66.12% | $7,076,319.63 |
| ONE/USDT:USDT | +28.65% | $53,734,660.17 |
| BTW/USDT:USDT | +26.30% | $2,132,939.46 |
| OFC/USDT:USDT | +23.23% | $2,469,920.78 |
| EVAA/USDT:USDT | +19.25% | $2,380,116.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.15% | +4.30% |
| ONE/USDT:USDT | below_1h_threshold | +4.13% | +4.28% |
| VVV/USDT:USDT | below_1h_threshold | +2.75% | +2.90% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.32% | +1.47% |
| ENA/USDT:USDT | below_1h_threshold | +0.37% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
