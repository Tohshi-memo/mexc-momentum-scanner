# Decision Report

- generated_at: 2026-08-20T01:16:16.356855+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12003**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=12003, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/15 | 33.3% | +2.69% | **+0.90%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.97% | **+0.58%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.76% | **+0.44%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.42% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +4.50% | **+1.80%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.81%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| MARKET_LONG | 20/20 | 100.0% | +0.46% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.47** / 初期 $100.00 (+505.47%)
- 確定: 4241件 (Win 1302 / Loss 1388 / Flat 1551) / skip 4323件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUU/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $605.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3593件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.97** / 初期 $100.00 (+16.97%)
- 確定: 1753件 (Win 520 / Loss 669 / Flat 564) / pending 0件 / skip 1721件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000488 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.97

## 6. Latest Market Context

- 更新: 2026-08-20T01:16:07.707532+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=69383.0
- Funnel: target 999 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +27.37% | $4,152,997.27 |
| TRUMPOFFICIAL/USDT:USDT | +23.57% | $14,654,741.97 |
| RE/USDT:USDT | +18.66% | $10,395,253.14 |
| ON/USDT:USDT | +14.06% | $4,772,654.01 |
| MRNASTOCK/USDT:USDT | +13.82% | $4,215,941.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CSOPSAMSUNG2L/USDT:USDT | below_1h_threshold | +4.11% | +4.12% |
| KOSPI/USDT:USDT | below_1h_threshold | +3.44% | +3.45% |
| KORU/USDT:USDT | below_1h_threshold | +3.35% | +3.35% |
| AKE/USDT:USDT | below_1h_threshold | +2.05% | +2.06% |
| BR/USDT:USDT | below_1h_threshold | +1.36% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
