# Decision Report

- generated_at: 2026-05-17T17:03:47.680862+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4412**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4412, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_BB3S | 5/11 | 45.5% | +1.22% | **+0.55%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.07% | **+0.05%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.04% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.02% | **+1.41%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.35% | **+0.74%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.98% | **+0.59%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.35** / 初期 $100.00 (+18.35%)
- 確定: 409件 (Win 105 / Loss 139 / Flat 165) / skip 564件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $118.35

## 4. Latest Market Context

- 更新: 2026-05-17T17:03:45.778281+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77977.6
- Funnel: target 760 → liquid 121 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +9.39% | $4,816,050.87 |
| UB/USDT:USDT | +5.65% | $11,635,171.03 |
| RAVE/USDT:USDT | +3.19% | $5,763,356.09 |
| KAIA/USDT:USDT | +2.82% | $4,290,891.34 |
| ARCSOL/USDT:USDT | +2.52% | $1,210,351.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +3.14% | +3.16% |
| B/USDT:USDT | below_1h_threshold | +0.77% | +0.79% |
| IRYS/USDT:USDT | below_1h_threshold | +0.48% | +0.50% |
| RUNE/USDT:USDT | below_1h_threshold | +0.47% | +0.49% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.38% | +0.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
