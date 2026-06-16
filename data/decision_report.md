# Decision Report

- generated_at: 2026-06-16T14:03:41.934063+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6867**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6867, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| ASK | 20/20 | 100.0% | -0.07% | **-0.07%** |
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.52% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +4.87% | **+3.89%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.53%** |
| ASK_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.18% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$185.91** / 初期 $100.00 (+85.91%)
- 確定: 1740件 (Win 457 / Loss 544 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPCXSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $185.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 122件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0351 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T14:03:36.869348+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=66169.9
- Funnel: target 777 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +48.46% | $4,100,215.30 |
| BSB/USDT:USDT | +46.96% | $34,322,729.34 |
| PORTAL/USDT:USDT | +32.78% | $3,596,961.58 |
| SPCXSTOCK/USDT:USDT | +27.97% | $644,363,586.01 |
| LAB/USDT:USDT | +26.95% | $16,562,432.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.56% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.05% | +1.81% |
| ROAM/USDT:USDT | below_1h_threshold | +1.49% | +1.25% |
| ARMSTOCK/USDT:USDT | below_1h_threshold | +1.00% | +0.76% |
| UNI/USDT:USDT | below_1h_threshold | +0.70% | +0.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
