# Decision Report

- generated_at: 2026-11-14T09:11:25.100527+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18883**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.06% / filled 20/20。**
- 全期間 MARKET基準: n=18883, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.91% | **+0.87%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.89% | **+0.85%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.50% | **+0.75%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.25% | **+0.63%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.57% | **+0.34%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.35% | **+0.32%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,763.10** / 初期 $100.00 (+1663.10%)
- 確定: 7291件 (Win 2100 / Loss 2337 / Flat 2854) / skip 8153件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,763.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$416.92** / 初期 $100.00 (+316.92%)
- 確定: 4891件 (Win 1310 / Loss 1078 / Flat 2503) / skip 7403件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1016 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $416.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7043件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000277 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-14T09:11:11.241853+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=67150.1
- Funnel: target 1071 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHELL/USDT:USDT | +52.92% | $4,432,503.80 |
| AKE/USDT:USDT | +26.86% | $77,446,640.62 |
| DODO/USDT:USDT | +18.35% | $1,401,627.72 |
| NIGHT/USDT:USDT | +4.69% | $1,326,343.12 |
| ARIA/USDT:USDT | +4.40% | $4,311,955.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DODO/USDT:USDT | below_1h_threshold | +3.03% | +2.76% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.67% | +0.40% |
| SHELL/USDT:USDT | below_1h_threshold | +0.54% | +0.27% |
| BERA/USDT:USDT | below_1h_threshold | +0.28% | +0.01% |
| TESLA/USDT:USDT | below_1h_threshold | +0.18% | -0.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
