# Decision Report

- generated_at: 2026-11-25T06:46:14.498990+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19598**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.53% / filled 20/20。**
- 全期間 MARKET基準: n=19598, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.53% | **+3.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.53% | **+3.53%** |
| LIMIT_1PCT | 17/20 | 85.0% | +3.21% | **+2.73%** |
| LIMIT_2PCT | 14/20 | 70.0% | +3.15% | **+2.20%** |
| LIMIT_ATR | 8/20 | 40.0% | +4.04% | **+1.61%** |
| LIMIT_3PCT | 10/20 | 50.0% | +2.31% | **+1.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.19% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 288件 (TP 105 / SL 175 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,988.31** / 初期 $100.00 (+1888.31%)
- 確定: 7610件 (Win 2191 / Loss 2450 / Flat 2969) / skip 8549件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.06% 残高後 $1,988.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.28** / 初期 $100.00 (+367.28%)
- 確定: 5220件 (Win 1389 / Loss 1124 / Flat 2707) / skip 7789件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $467.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7757件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000391 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-25T06:46:01.925098+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=59170.0
- Funnel: target 1092 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIGTIME/USDT:USDT | +46.26% | $1,973,045.12 |
| OPG/USDT:USDT | +21.97% | $2,140,890.05 |
| BTW/USDT:USDT | +15.94% | $5,003,055.31 |
| GUA/USDT:USDT | +14.52% | $2,140,010.31 |
| ANSEM/USDT:USDT | +8.83% | $1,436,667.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MONAD/USDT:USDT | below_1h_threshold | +2.20% | +2.14% |
| ACE/USDT:USDT | below_1h_threshold | +2.14% | +2.08% |
| SOXS/USDT:USDT | below_1h_threshold | +1.62% | +1.56% |
| XPL/USDT:USDT | below_1h_threshold | +1.60% | +1.54% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +1.59% | +1.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
