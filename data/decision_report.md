# Decision Report

- generated_at: 2026-05-31T19:20:56.588592+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5217**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5217, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.81% | **-1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.08% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.00% | **+4.00%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +4.01% | **+2.40%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.65% | **+2.19%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.63% | **+1.81%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.26% | **+1.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.17** / 初期 $100.00 (+31.17%)
- 確定: 852件 (Win 198 / Loss 253 / Flat 401) / skip 926件
- 成長率目線: 平均log +0.000318 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $131.17

## 4. Latest Market Context

- 更新: 2026-05-31T19:20:53.805133+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=73587.5
- Funnel: target 773 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +35.95% | $11,643,157.68 |
| BSB/USDT:USDT | +11.32% | $4,600,863.01 |
| HOME/USDT:USDT | +9.86% | $2,496,141.01 |
| UB/USDT:USDT | +8.21% | $6,723,490.76 |
| SKYAI/USDT:USDT | +6.33% | $4,914,147.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.98% | +3.96% |
| BSB/USDT:USDT | below_1h_threshold | +1.64% | +1.62% |
| AIA/USDT:USDT | below_1h_threshold | +1.36% | +1.35% |
| PORTAL/USDT:USDT | below_1h_threshold | +0.80% | +0.78% |
| UB/USDT:USDT | below_1h_threshold | +0.74% | +0.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
