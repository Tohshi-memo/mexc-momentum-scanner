# Decision Report

- generated_at: 2026-08-15T05:51:37.246816+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11638**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=11638, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.56% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.96% | **+0.63%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.75% | **+0.61%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.88% | **+0.53%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$636.46** / 初期 $100.00 (+536.46%)
- 確定: 4106件 (Win 1285 / Loss 1352 / Flat 1469) / skip 4093件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $636.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$153.87** / 初期 $100.00 (+53.87%)
- 確定: 1701件 (Win 487 / Loss 409 / Flat 805) / skip 3348件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0336 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $153.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.76** / 初期 $100.00 (+17.76%)
- 確定: 1583件 (Win 481 / Loss 604 / Flat 498) / pending 6件 / skip 1523件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000176 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $117.76

## 6. Latest Market Context

- 更新: 2026-08-15T05:51:22.400215+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=63028.6
- Funnel: target 985 → liquid 166 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +32.86% | $5,066,055.11 |
| ONE/USDT:USDT | +21.27% | $1,576,000.06 |
| ANSEM/USDT:USDT | +21.01% | $1,013,836.03 |
| PRL/USDT:USDT | +20.09% | $1,052,273.57 |
| US/USDT:USDT | +19.68% | $6,502,025.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOLO/USDT:USDT | below_1h_threshold | +4.77% | +4.87% |
| US/USDT:USDT | below_1h_threshold | +4.37% | +4.47% |
| NIL/USDT:USDT | below_1h_threshold | +4.33% | +4.43% |
| ONE/USDT:USDT | below_1h_threshold | +4.27% | +4.37% |
| VELVET/USDT:USDT | below_1h_threshold | +3.73% | +3.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
