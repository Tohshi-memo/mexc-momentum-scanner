# Decision Report

- generated_at: 2026-05-31T23:39:18.029125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5239**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5239, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.10% | **+1.09%** |
| LIMIT_BB3S | 4/11 | 36.4% | +0.84% | **+0.30%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.32% | **-0.16%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.19% | **+1.97%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +3.58% | **+1.59%** |
| ASK_LONG | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.90% | **+1.42%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.67** / 初期 $100.00 (+34.67%)
- 確定: 874件 (Win 204 / Loss 259 / Flat 411) / skip 926件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.90% 残高後 $134.67

## 4. Latest Market Context

- 更新: 2026-05-31T23:39:15.825054+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.52% price=73537.0
- Funnel: target 774 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +123.39% | $18,825,456.32 |
| STG/USDT:USDT | +41.01% | $20,661,557.09 |
| H/USDT:USDT | +15.73% | $12,352,191.42 |
| HOME/USDT:USDT | +14.05% | $3,207,540.55 |
| ZORA/USDT:USDT | +12.27% | $1,634,618.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +1.57% | +2.08% |
| LAB/USDT:USDT | below_1h_threshold | +1.42% | +1.93% |
| AIA/USDT:USDT | below_1h_threshold | +1.39% | +1.91% |
| MEME/USDT:USDT | below_1h_threshold | +1.13% | +1.64% |
| ID/USDT:USDT | below_1h_threshold | +0.60% | +1.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
