# Decision Report

- generated_at: 2026-11-04T19:41:48.499549+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18134**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18134, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.98% | **-1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.69% | **+0.17%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.97% | **+3.97%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.77% | **+1.60%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.19% | **+1.43%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.92** / 初期 $100.00 (+1431.92%)
- 確定: 6953件 (Win 2012 / Loss 2229 / Flat 2712) / skip 7742件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,531.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$378.49** / 初期 $100.00 (+278.49%)
- 確定: 4544件 (Win 1220 / Loss 1021 / Flat 2303) / skip 7001件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $378.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6299件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T19:41:35.502998+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=80120.5
- Funnel: target 1078 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +23.05% | $12,680,594.82 |
| AIN/USDT:USDT | +13.19% | $2,524,801.14 |
| FLUID/USDT:USDT | +6.89% | $2,020,097.72 |
| LYN/USDT:USDT | +5.79% | $1,082,116.33 |
| CRCLSTOCK/USDT:USDT | +3.49% | $36,931,396.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +3.13% | +3.37% |
| AXIS/USDT:USDT | below_1h_threshold | +2.37% | +2.61% |
| HOT/USDT:USDT | below_1h_threshold | +1.94% | +2.18% |
| LYN/USDT:USDT | below_1h_threshold | +0.80% | +1.05% |
| ARIA/USDT:USDT | below_1h_threshold | +0.76% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
