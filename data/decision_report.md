# Decision Report

- generated_at: 2026-06-16T17:55:45.174901+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6876**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6876, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.96% | **+0.24%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.23% | **+0.07%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |
| ASK | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +3.85% | **+3.30%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.92% | **+1.54%** |
| ASK_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.07% | **+0.91%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.19% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$186.82** / 初期 $100.00 (+86.82%)
- 確定: 1749件 (Win 462 / Loss 548 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000357 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $186.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 131件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0398 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T17:55:40.939003+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=65903.9
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +12.42% | $24,289,764.91 |
| H/USDT:USDT | +10.08% | $63,355,895.27 |
| STG/USDT:USDT | +9.07% | $3,466,936.49 |
| TRIA/USDT:USDT | +8.05% | $1,063,040.06 |
| BSB/USDT:USDT | +7.29% | $39,407,666.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_relative_strength | +5.07% | +4.81% |
| VELVET/USDT:USDT | below_1h_threshold | +4.32% | +4.06% |
| COAI/USDT:USDT | below_1h_threshold | +4.18% | +3.91% |
| XPL/USDT:USDT | below_1h_threshold | +4.02% | +3.76% |
| CHIP/USDT:USDT | below_1h_threshold | +3.49% | +3.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
