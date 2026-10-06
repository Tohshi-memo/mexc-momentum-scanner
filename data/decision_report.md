# Decision Report

- generated_at: 2026-10-06T03:21:34.466761+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16180**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=16180, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.41% | **+1.27%** |
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.02% | **+0.56%** |
| LIMIT_BB3S | 2/18 | 11.1% | +4.91% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.61% | **+5.61%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.41% | **+0.92%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.98% | **+0.64%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.22% | **+0.10%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定トレード: 230件 (TP 82 / SL 141 / EXP 7)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,271.40** / 初期 $100.00 (+1171.40%)
- 確定: 6237件 (Win 1825 / Loss 1994 / Flat 2418) / skip 6504件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FLUID/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,271.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3611件 (Win 1005 / Loss 845 / Flat 1761) / skip 5980件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0204 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RLC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4337件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T03:21:22.995384+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=85508.0
- Funnel: target 1074 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +29.23% | $20,263,722.30 |
| ORCA/USDT:USDT | +19.12% | $2,131,791.68 |
| CHIP/USDT:USDT | +9.08% | $2,083,455.25 |
| FILECOIN/USDT:USDT | +7.30% | $14,941,296.30 |
| RAY/USDT:USDT | +7.15% | $5,077,725.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RLC/USDT:USDT | below_1h_threshold | +2.22% | +2.21% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.40% | +1.38% |
| VELVET/USDT:USDT | below_1h_threshold | +0.79% | +0.77% |
| DOT/USDT:USDT | below_1h_threshold | +0.69% | +0.67% |
| ATOM/USDT:USDT | below_1h_threshold | +0.67% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
