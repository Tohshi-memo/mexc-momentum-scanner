# Decision Report

- generated_at: 2026-11-14T12:01:13.083174+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18893**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=18893, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_BB3S | 9/16 | 56.2% | +0.98% | **+0.55%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.50% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.60% | **+0.91%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +1.09% | **+0.38%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.57% | **+0.34%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,760.31** / 初期 $100.00 (+1660.31%)
- 確定: 7297件 (Win 2102 / Loss 2340 / Flat 2855) / skip 8157件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,760.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$419.72** / 初期 $100.00 (+319.72%)
- 確定: 4901件 (Win 1312 / Loss 1080 / Flat 2509) / skip 7403件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0687 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $419.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7053件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-14T12:01:01.986743+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=67286.1
- Funnel: target 1071 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHELL/USDT:USDT | +34.43% | $4,933,176.73 |
| DODO/USDT:USDT | +25.94% | $1,707,672.53 |
| AKE/USDT:USDT | +21.45% | $82,018,444.48 |
| SOPH/USDT:USDT | +11.32% | $1,600,031.20 |
| ARIA/USDT:USDT | +9.61% | $3,876,473.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +0.81% | +0.74% |
| SOPH/USDT:USDT | below_1h_threshold | +0.67% | +0.61% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.55% | +0.49% |
| JUP/USDT:USDT | below_1h_threshold | +0.42% | +0.36% |
| BLESS/USDT:USDT | below_1h_threshold | +0.33% | +0.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
