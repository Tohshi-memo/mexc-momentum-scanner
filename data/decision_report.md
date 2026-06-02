# Decision Report

- generated_at: 2026-06-02T03:09:36.752120+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5392**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.29% / filled 20/20。**
- 全期間 MARKET基準: n=5392, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.29% | **+1.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.65% | **+1.46%** |
| MARKET | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.77% | **+0.38%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.29% | **+0.19%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.65% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.98** / 初期 $100.00 (+31.98%)
- 確定: 905件 (Win 211 / Loss 271 / Flat 423) / skip 1048件
- 成長率目線: 平均log +0.000307 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.98

## 4. Latest Market Context

- 更新: 2026-06-02T03:09:34.116933+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=70932.3
- Funnel: target 776 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +25.47% | $10,679,974.00 |
| LAB/USDT:USDT | +16.69% | $193,934,540.66 |
| H/USDT:USDT | +16.10% | $55,976,764.07 |
| WLD/USDT:USDT | +14.86% | $135,059,839.53 |
| PIEVERSE/USDT:USDT | +14.41% | $1,799,628.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +1.64% | +1.48% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.54% | +1.38% |
| LIT/USDT:USDT | below_1h_threshold | +1.37% | +1.21% |
| WLD/USDT:USDT | below_1h_threshold | +1.16% | +1.00% |
| JUP/USDT:USDT | below_1h_threshold | +0.94% | +0.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
