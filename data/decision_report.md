# Decision Report

- generated_at: 2026-11-04T20:51:32.720953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18137**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18137, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.39% | **-1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.80% | **+0.84%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.69% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.64% | **+1.56%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.70% | **+1.08%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.36% | **+1.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.81** / 初期 $100.00 (+1431.81%)
- 確定: 6956件 (Win 2013 / Loss 2231 / Flat 2712) / skip 7742件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,531.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$378.43** / 初期 $100.00 (+278.43%)
- 確定: 4547件 (Win 1221 / Loss 1023 / Flat 2303) / skip 7001件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $378.43

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6302件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T20:51:19.926377+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=80065.8
- Funnel: target 1078 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +35.03% | $15,022,712.31 |
| FLUID/USDT:USDT | +10.71% | $2,403,831.60 |
| AIN/USDT:USDT | +8.58% | $2,565,534.31 |
| DGAI/USDT:USDT | +6.49% | $1,106,616.54 |
| AXTISTOCK/USDT:USDT | +4.43% | $2,259,475.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLUID/USDT:USDT | below_1h_threshold | +3.23% | +3.10% |
| SYRUP/USDT:USDT | below_1h_threshold | +2.81% | +2.67% |
| WLFI/USDT:USDT | below_1h_threshold | +1.94% | +1.80% |
| BR/USDT:USDT | below_1h_threshold | +1.78% | +1.65% |
| RAY/USDT:USDT | below_1h_threshold | +0.85% | +0.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
