# Decision Report

- generated_at: 2026-06-02T08:15:12.227882+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5426**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5426, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 12/18 | 66.7% | +0.70% | **+0.47%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.67% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.90% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.97% | **+0.68%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.93% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$96.63** / 初期 $100.00 (-3.37%)
- 確定トレード: 84件 (TP 24 / SL 57 / EXP 3)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.63
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.78** / 初期 $100.00 (+33.78%)
- 確定: 938件 (Win 220 / Loss 281 / Flat 437) / skip 1049件
- 成長率目線: 平均log +0.000310 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MRVLSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $133.78

## 4. Latest Market Context

- 更新: 2026-06-02T08:15:09.163322+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=70034.6
- Funnel: target 772 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1, 4h RSI 81.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +44.50% | $1,832,440.64 |
| SKYAI/USDT:USDT | +41.73% | $16,394,559.27 |
| ESPORTS/USDT:USDT | +29.52% | $12,256,714.21 |
| MRVLSTOCK/USDT:USDT | +26.06% | $2,928,421.12 |
| H/USDT:USDT | +21.20% | $58,170,387.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +4.60% | +4.67% |
| JTO/USDT:USDT | below_1h_threshold | +3.60% | +3.67% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.42% | +3.49% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.50% | +2.56% |
| MYX/USDT:USDT | below_1h_threshold | +2.21% | +2.27% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
