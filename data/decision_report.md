# Decision Report

- generated_at: 2026-06-01T11:04:40.757431+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5309**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=5309, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +2.12% | **+1.80%** |
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.03% | **+0.93%** |
| ASK | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.53% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.77% | **+0.39%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.09% | **+0.08%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 976件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T11:04:38.338446+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=72708.7
- Funnel: target 776 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +140.57% | $35,885,310.71 |
| SLX/USDT:USDT | +100.93% | $7,429,450.65 |
| H/USDT:USDT | +91.86% | $32,365,737.34 |
| LAB/USDT:USDT | +71.94% | $221,343,001.98 |
| VIC/USDT:USDT | +68.11% | $1,011,082.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MERL/USDT:USDT | below_1h_threshold | +2.30% | +2.33% |
| CTR/USDT:USDT | below_1h_threshold | +2.25% | +2.27% |
| HOME/USDT:USDT | below_1h_threshold | +2.01% | +2.03% |
| LAB/USDT:USDT | below_1h_threshold | +1.98% | +2.00% |
| IBMSTOCK/USDT:USDT | below_1h_threshold | +1.92% | +1.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
