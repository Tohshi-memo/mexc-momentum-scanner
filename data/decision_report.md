# Decision Report

- generated_at: 2026-08-15T04:16:23.128739+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11632**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=11632, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.18% | **+1.01%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.33% | **+0.67%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.11% | **-0.04%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.61% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$639.66** / 初期 $100.00 (+539.66%)
- 確定: 4100件 (Win 1285 / Loss 1351 / Flat 1464) / skip 4093件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROBO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $639.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.60** / 初期 $100.00 (+52.60%)
- 確定: 1695件 (Win 484 / Loss 409 / Flat 802) / skip 3348件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0476 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $152.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.31** / 初期 $100.00 (+17.31%)
- 確定: 1577件 (Win 479 / Loss 604 / Flat 494) / pending 3件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000131 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $117.31

## 6. Latest Market Context

- 更新: 2026-08-15T04:16:14.514591+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=63082.4
- Funnel: target 985 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +34.34% | $3,098,523.26 |
| AIO/USDT:USDT | +19.11% | $1,398,487.75 |
| US/USDT:USDT | +16.27% | $6,797,092.82 |
| ONE/USDT:USDT | +14.13% | $1,535,808.22 |
| VELVET/USDT:USDT | +11.45% | $46,240,688.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +3.23% | +3.15% |
| US/USDT:USDT | below_1h_threshold | +2.94% | +2.85% |
| NIL/USDT:USDT | below_1h_threshold | +1.22% | +1.13% |
| PYTH/USDT:USDT | below_1h_threshold | +0.68% | +0.59% |
| WLFI/USDT:USDT | below_1h_threshold | +0.60% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
