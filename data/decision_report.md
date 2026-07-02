# Decision Report

- generated_at: 2026-07-02T09:27:31.396109+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8056**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.80% / filled 20/20。**
- 全期間 MARKET基準: n=8056, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |
| ASK | 20/20 | 100.0% | +3.79% | **+3.79%** |
| LIMIT_1PCT | 12/20 | 60.0% | +1.17% | **+0.70%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_2PCT | 10/20 | 50.0% | +0.62% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +2.16% | **+0.76%** |
| LIMIT_9PCT_LONG | 10/20 | 50.0% | +0.26% | **+0.13%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.46% | **-0.12%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | -1.02% | **-0.77%** |

## 2. $100 Live Portfolio

- 残高: **$103.66** / 初期 $100.00 (+3.66%)
- 確定トレード: 48件 (TP 18 / SL 29 / EXP 1)
- 最新: TLM/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.66
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2173件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 546件 (Win 136 / Loss 131 / Flat 279) / skip 921件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0466 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T09:27:24.235663+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=60540.6
- Funnel: target 829 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +59.14% | $5,458,534.14 |
| BREV/USDT:USDT | +45.94% | $2,802,727.63 |
| RIF/USDT:USDT | +28.39% | $5,873,717.43 |
| TAIKO/USDT:USDT | +26.74% | $100,917,264.50 |
| TLM/USDT:USDT | +23.25% | $8,699,235.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIRB/USDT:USDT | below_1h_threshold | +2.67% | +2.59% |
| GRAM/USDT:USDT | below_1h_threshold | +2.64% | +2.55% |
| H/USDT:USDT | below_1h_threshold | +2.43% | +2.34% |
| SLX/USDT:USDT | below_1h_threshold | +1.35% | +1.26% |
| BEAT/USDT:USDT | below_1h_threshold | +1.03% | +0.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
