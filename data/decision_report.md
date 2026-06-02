# Decision Report

- generated_at: 2026-06-02T06:46:33.394596+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5415**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5415, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.08% | **+0.46%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.70% | **+2.43%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.04% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK_LONG | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.63% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.68** / 初期 $100.00 (+37.68%)
- 確定: 927件 (Win 219 / Loss 274 / Flat 434) / skip 1049件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $137.68

## 4. Latest Market Context

- 更新: 2026-06-02T06:46:28.128030+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=70256.0
- Funnel: target 777 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1, 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +51.55% | $11,030,295.36 |
| US/USDT:USDT | +39.21% | $1,149,435.00 |
| ESPORTS/USDT:USDT | +28.33% | $11,960,320.26 |
| OPG/USDT:USDT | +23.41% | $1,078,769.66 |
| LAB/USDT:USDT | +22.12% | $218,396,483.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.98% | +4.95% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.45% | +3.43% |
| MYX/USDT:USDT | below_1h_threshold | +3.44% | +3.41% |
| UAI/USDT:USDT | below_1h_threshold | +3.09% | +3.06% |
| UB/USDT:USDT | below_1h_threshold | +2.13% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
