# Decision Report

- generated_at: 2026-06-01T00:05:24.680184+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5240**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5240, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.30% | **+0.99%** |
| LIMIT_BB3S | 4/11 | 36.4% | +0.84% | **+0.30%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.00% | **-0.00%** |
| ASK | 20/20 | 100.0% | -0.14% | **-0.14%** |
| LIMIT_10PCT | 4/20 | 20.0% | -1.00% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +3.58% | **+1.59%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.68% | **+1.52%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.53% | **+1.22%** |
| ASK_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.99** / 初期 $100.00 (+33.99%)
- 確定: 875件 (Win 204 / Loss 260 / Flat 411) / skip 926件
- 成長率目線: 平均log +0.000334 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PORTAL/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $133.99

## 4. Latest Market Context

- 更新: 2026-06-01T00:05:22.113129+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=73850.0
- Funnel: target 774 → liquid 131 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +114.10% | $19,937,270.24 |
| STG/USDT:USDT | +38.56% | $20,989,132.23 |
| H/USDT:USDT | +20.23% | $12,334,893.25 |
| HOME/USDT:USDT | +17.15% | $3,255,941.26 |
| ZORA/USDT:USDT | +12.37% | $1,640,091.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +3.20% | +2.93% |
| ZEC/USDT:USDT | below_1h_threshold | +1.36% | +1.09% |
| H/USDT:USDT | below_1h_threshold | +1.28% | +1.01% |
| LIT/USDT:USDT | below_1h_threshold | +1.18% | +0.91% |
| WLD/USDT:USDT | below_1h_threshold | +1.11% | +0.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
