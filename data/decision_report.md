# Decision Report

- generated_at: 2026-06-12T01:45:34.462776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6442**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6442, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +6.46% | **+0.65%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.02% | **+0.02%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.79% | **+0.59%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.66% | **+0.53%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.80% | **+0.52%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.52% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1676件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T01:45:31.031872+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=63374.6
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +100.11% | $131,178,380.89 |
| ESPORTS/USDT:USDT | +44.56% | $26,695,097.19 |
| CLO/USDT:USDT | +20.65% | $1,205,119.97 |
| NAORIS/USDT:USDT | +18.77% | $1,442,412.17 |
| SKYAI/USDT:USDT | +18.55% | $13,456,691.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XMR/USDT:USDT | below_1h_threshold | +4.42% | +4.80% |
| NAORIS/USDT:USDT | below_1h_threshold | +4.07% | +4.45% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.69% | +4.07% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.79% | +3.17% |
| STG/USDT:USDT | below_1h_threshold | +1.58% | +1.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
