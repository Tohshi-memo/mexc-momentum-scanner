# Decision Report

- generated_at: 2026-10-06T11:26:26.495795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16199**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16199, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +2.69% | **+0.67%** |
| LIMIT_9PCT | 5/20 | 25.0% | +1.83% | **+0.46%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.01% | **+0.40%** |
| LIMIT_BB3S | 6/17 | 35.3% | -0.45% | **-0.16%** |
| LIMIT_8PCT | 5/20 | 25.0% | -0.92% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.40% | **+3.40%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.03% | **+2.27%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.84% | **+1.92%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.75% | **+0.96%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.07% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定トレード: 230件 (TP 82 / SL 141 / EXP 7)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,303.41** / 初期 $100.00 (+1203.41%)
- 確定: 6242件 (Win 1829 / Loss 1995 / Flat 2418) / skip 6518件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLC/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,303.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3611件 (Win 1005 / Loss 845 / Flat 1761) / skip 5999件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RLC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4360件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000097 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T11:26:14.434689+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=86209.9
- Funnel: target 1074 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +88.12% | $35,678,831.56 |
| US/USDT:USDT | +42.81% | $1,202,953.52 |
| ORCA/USDT:USDT | +34.04% | $3,269,577.25 |
| BR/USDT:USDT | +32.84% | $42,498,382.20 |
| API3/USDT:USDT | +28.55% | $2,503,058.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| API3/USDT:USDT | below_1h_threshold | +3.98% | +3.88% |
| ORCA/USDT:USDT | below_1h_threshold | +3.89% | +3.78% |
| CAP/USDT:USDT | below_1h_threshold | +2.07% | +1.96% |
| CHIP/USDT:USDT | below_1h_threshold | +1.31% | +1.20% |
| US/USDT:USDT | below_1h_threshold | +1.28% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
