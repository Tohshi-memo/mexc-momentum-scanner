# Decision Report

- generated_at: 2026-11-16T05:06:06.934819+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18995**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=18995, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.09% | **+0.41%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.49% | **+0.20%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.13% | **+0.10%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/8 | 37.5% | +2.76% | **+1.04%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.98% | **+0.73%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.52% | **+0.39%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.24% | **+0.15%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.06% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,720.18** / 初期 $100.00 (+1620.18%)
- 確定: 7337件 (Win 2107 / Loss 2349 / Flat 2881) / skip 8219件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BARD/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $1,720.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$429.80** / 初期 $100.00 (+329.80%)
- 確定: 4982件 (Win 1331 / Loss 1081 / Flat 2570) / skip 7424件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BARD/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $429.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7155件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000088 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T05:05:58.301866+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=64654.3
- Funnel: target 1066 → liquid 114 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +65.25% | $6,430,961.71 |
| SKR/USDT:USDT | +35.62% | $1,609,414.70 |
| SHELL/USDT:USDT | +12.41% | $1,524,497.65 |
| PIEVERSE/USDT:USDT | +6.91% | $1,915,943.03 |
| MSTRSTOCK/USDT:USDT | +3.41% | $8,807,159.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.36% | +1.57% |
| ZRO/USDT:USDT | below_1h_threshold | +0.56% | +0.77% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.16% | +0.37% |
| XLV/USDT:USDT | below_1h_threshold | +0.16% | +0.37% |
| ASTER/USDT:USDT | below_1h_threshold | +0.09% | +0.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
