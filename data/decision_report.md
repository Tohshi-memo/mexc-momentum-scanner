# Decision Report

- generated_at: 2026-05-20T09:33:51.606537+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4535**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4535, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.79% | **-0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.49% | **+0.32%** |
| LIMIT_5PCT | 6/20 | 30.0% | -0.70% | **-0.21%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.06% | **-0.21%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.73% | **-0.26%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.61% | **-0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.76% | **+1.76%** |
| ASK_LONG | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.47% | **+0.19%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.38% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.02** / 初期 $100.00 (+25.02%)
- 確定: 497件 (Win 130 / Loss 170 / Flat 197) / skip 599件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $125.02

## 4. Latest Market Context

- 更新: 2026-05-20T09:33:43.974712+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=77499.9
- Funnel: target 762 → liquid 132 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +104.00% | $1,392,964.41 |
| FIDA/USDT:USDT | +36.17% | $2,689,887.73 |
| PROMPT/USDT:USDT | +35.78% | $12,478,779.33 |
| LIT/USDT:USDT | +26.77% | $8,561,341.81 |
| EDEN/USDT:USDT | +24.57% | $21,583,256.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +2.77% | +2.67% |
| DASH/USDT:USDT | below_1h_threshold | +2.49% | +2.40% |
| HOME/USDT:USDT | below_1h_threshold | +2.02% | +1.93% |
| ZEN/USDT:USDT | below_1h_threshold | +1.94% | +1.85% |
| LIT/USDT:USDT | below_1h_threshold | +1.93% | +1.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
