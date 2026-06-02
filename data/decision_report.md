# Decision Report

- generated_at: 2026-06-02T03:35:58.743077+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5397**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.02% / filled 20/20。**
- 全期間 MARKET基準: n=5397, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.54% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.80% | **+0.99%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.77% | **+0.38%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.50% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.76** / 初期 $100.00 (+31.76%)
- 確定: 909件 (Win 211 / Loss 272 / Flat 426) / skip 1049件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $131.76

## 4. Latest Market Context

- 更新: 2026-06-02T03:35:55.148639+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=70932.3
- Funnel: target 776 → liquid 147 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.8 >= 65=1, 4h RSI 66.1 >= 65=1, 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +21.69% | $1,212,430.30 |
| LAB/USDT:USDT | +20.80% | $197,772,295.25 |
| ESPORTS/USDT:USDT | +20.23% | $10,832,937.89 |
| WLD/USDT:USDT | +18.55% | $136,841,407.79 |
| SKYAI/USDT:USDT | +18.42% | $4,016,641.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.93% | +4.77% |
| WLD/USDT:USDT | below_1h_threshold | +4.48% | +4.32% |
| LAB/USDT:USDT | below_1h_threshold | +4.37% | +4.21% |
| EPIC/USDT:USDT | below_1h_threshold | +3.69% | +3.52% |
| STG/USDT:USDT | below_1h_threshold | +3.48% | +3.32% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
