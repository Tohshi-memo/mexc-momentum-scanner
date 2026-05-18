# Decision Report

- generated_at: 2026-05-18T05:59:11.764113+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4437**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4437, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.24% | **+0.09%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| ASK | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.71% | **+1.71%** |
| MARKET_LONG | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.03% | **+0.72%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.54% | **+0.32%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.47% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$96.22** / 初期 $100.00 (-3.78%)
- 確定トレード: 52件 (TP 13 / SL 36 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.70** / 初期 $100.00 (+21.70%)
- 確定: 434件 (Win 113 / Loss 147 / Flat 174) / skip 564件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $121.70

## 4. Latest Market Context

- 更新: 2026-05-18T05:59:09.359907+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=76872.7
- Funnel: target 765 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1, 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +44.50% | $6,592,776.76 |
| BSB/USDT:USDT | +8.25% | $19,711,401.17 |
| AKT/USDT:USDT | +5.27% | $1,519,125.96 |
| OPENLEDGER/USDT:USDT | +5.24% | $1,295,146.77 |
| HYPE/USDT:USDT | +4.28% | $282,175,636.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +3.05% | +3.22% |
| GUA/USDT:USDT | below_1h_threshold | +1.38% | +1.55% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.16% | +0.33% |
| RUNE/USDT:USDT | below_1h_threshold | +0.14% | +0.30% |
| SPX500/USDT:USDT | below_1h_threshold | +0.07% | +0.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
